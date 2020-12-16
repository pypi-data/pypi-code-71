# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~IMPORTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Standard library imports
from collections import *
import warnings

# Third party imports
import numpy as np
import pandas as pd
import pysam as ps

# Local lib import
from pycoQC.common import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GLOBAL SETTINGS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Silence futurewarnings
warnings.filterwarnings("ignore", category=FutureWarning)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN CLASS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class pycoQC_parse ():

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~INIT METHOD~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def __init__ (self,
        summary_file:str,
        barcode_file:str="",
        bam_file:str="",
        runid_list:list=[],
        filter_calibration:bool=False,
        filter_duplicated:bool=False,
        min_barcode_percent:float=0.1,
        cleanup:bool=True,
        verbose:bool=False,
        quiet:bool=False):
        """
        Parse Albacore sequencing_summary.txt file and clean-up the data
        * summary_file
            Path to the sequencing_summary generated by Albacore 1.0.0 + (read_fast5_basecaller.py) / Guppy 2.1.3+ (guppy_basecaller).
            One can also pass multiple space separated file paths or a UNIX style regex matching multiple files
        * barcode_file
            Path to the barcode_file generated by Guppy 2.1.3+ (guppy_barcoder) or Deepbinner 0.2.0+. This is not a required file.
            One can also pass multiple space separated file paths or a UNIX style regex matching multiple files
        * bam_file
            Path to a Bam file corresponding to reads in the summary_file. Preferably aligned with Minimap2
            One can also pass multiple space separated file paths or a UNIX style regex matching multiple files
        * runid_list
            Select only specific runids to be analysed. Can also be used to force pycoQC to order the runids for
            temporal plots, if the sequencing_summary file contain several sucessive runs. By default pycoQC analyses
            all the runids in the file and uses the runid order as defined in the file.
        * filter_calibration
            If True read flagged as calibration strand by the software are removed
        * filter_duplicated
            If True duplicated read_ids are removed but the first occurence is kept (Guppy sometimes outputs the same read multiple times)
        * min_barcode_percent
            Minimal percent of total reads to retain barcode label. If below the barcode value is set as `unclassified`.
        """

        # Set logging level
        self.logger = get_logger(name=__name__, verbose=verbose, quiet=quiet)

        # Save self variables
        self.runid_list = runid_list
        self.filter_calibration = filter_calibration
        self.filter_duplicated = filter_duplicated
        self.min_barcode_percent = min_barcode_percent
        self.cleanup = cleanup

        # Init object counter
        self.counter = OrderedDict()

        # Check input files
        self.logger.warning ("Check input data files")

        # Expand file names and test readability
        self.summary_files_list = expand_file_names(summary_file)
        self.logger.debug ("\t\tSequencing summary files found: {}".format(" ".join(self.summary_files_list)))
        self.counter["Summary files found"] = len(self.summary_files_list)

        if barcode_file:
            self.barcode_files_list = expand_file_names(barcode_file)
            self.logger.debug ("\t\tBarcode files found: {}".format(" ".join(self.barcode_files_list)))
            self.counter["Barcode files found"] = len(self.barcode_files_list)
        else:
            self.barcode_files_list =[]

        if bam_file:
            self.bam_file_list = expand_file_names(bam_file, bam_check=True)
            self.logger.debug ("\t\tBam files found: {}".format(" ".join(self.bam_file_list)))
            self.counter["Bam files found"] = len(self.bam_file_list)
        else:
            self.bam_file_list =[]

        self.logger.warning ("Parse data files")
        summary_reads_df = self._parse_summary()
        barcode_reads_df = self._parse_barcode()
        bam_reads_df, self.alignments_df, self.ref_len_dict = self._parse_bam()

        self.logger.warning ("Merge data")
        self.reads_df = self._merge_reads_df(summary_reads_df, barcode_reads_df, bam_reads_df)

        # Cleanup data
        if self.cleanup:
            self.logger.warning("Cleaning data")
            self.reads_df = self._clean_reads_df(self.reads_df)

    def __str__(self):
        return dict_to_str(self.counter)

    def __repr__(self):
        return "[{}]\n".format(self.__class__.__name__)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PRIVATE METHODS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    def _parse_summary (self):
        """"""
        self.logger.debug ("\tParse summary files")
        df = merge_files_to_df (self.summary_files_list)

        if self.cleanup:
            # Standardise col names for all types of files
            self.logger.debug ("\tRename summary sequencing columns")
            rename_colmanes = {
                "sequence_length_template":"read_len",
                "sequence_length_2d":"read_len",
                "sequence_length":"read_len",
                "mean_qscore_template":"mean_qscore",
                "mean_qscore_2d":"mean_qscore",
                "calibration_strand_genome_template":"calibration",
                "barcode_arrangement":"barcode"}
            df = df.rename(columns=rename_colmanes)

            # Verify the required and optional columns, Drop unused fields
            self.logger.debug ("\tVerifying fields and discarding unused columns")
            df = self._select_df_columns (
                df = df,
                required_colnames = ["read_id", "run_id", "channel", "start_time", "read_len", "mean_qscore"],
                optional_colnames = ["calibration", "barcode"])

        # Collect stats
        n = len(df)
        self.logger.debug ("\t\t{:,} reads found in initial file".format(n))
        self.counter["Initial reads"] = n

        return df

    def _parse_barcode (self):
        """"""
        if not self.barcode_files_list:
            return pd.DataFrame()

        self.logger.debug ("\tParse barcode files")
        df = merge_files_to_df (self.barcode_files_list)

        # check presence of barcode details
        if "read_id" in df and "barcode_arrangement" in df:
            self.logger.debug ("\t\tFound valid Guppy barcode file")
            df = df [["read_id", "barcode_arrangement"]]
            df = df.rename(columns={"barcode_arrangement":"barcode"})

        elif "read_ID" in df and "barcode_call" in df:
            self.logger.debug ("\t\tFound valid Deepbinner barcode file")
            df = df [["read_ID", "barcode_call"]]
            df = df.rename(columns={"read_ID":"read_id", "barcode_call":"barcode"})
            df['barcode'].replace("none", "unclassified", inplace=True)
        else:
            raise pycoQCError ("File {} does not contain required barcode information".format(fp))

        n = len(df[df['barcode']!="unclassified"])
        self.logger.debug ("\t\t{:,} reads with barcodes assigned".format(n))
        self.counter["Reads with barcodes"] = n

        return df

    def _parse_bam (self):
        """"""
        if not self.bam_file_list:
            return (pd.DataFrame(), pd.DataFrame(), OrderedDict())

        # Init collections
        ref_len_dict = OrderedDict()
        alignments_dict = Counter()
        read_dict = OrderedDict ()

        for bam_fn in self.bam_file_list:
            with ps.AlignmentFile(bam_fn, "rb") as bam:

                # Save reference lengths information
                for ref_id, ref_len in zip(bam.references, bam.lengths):
                    if not ref_id in ref_len_dict:
                        ref_len_dict[ref_id] = ref_len

                # Parse reads
                for read in bam:
                    if read.is_unmapped:
                        alignments_dict["Unmapped"]+=1
                    elif read.is_secondary:
                        alignments_dict["Secondary"]+=1
                    elif read.is_supplementary:
                        alignments_dict["Suplementary"]+=1
                    elif read.query_name in read_dict:
                        alignments_dict["Duplicated"]+=1
                    else:
                        alignments_dict["Primary"]+=1
                        read_dict[read.query_name] = self._get_read_stats(read)

        # Convert aligments_dict to df
        if alignments_dict:
            alignments_df = pd.DataFrame.from_dict(alignments_dict, orient="index")
            alignments_df.reset_index(inplace=True)
            alignments_df.columns=["Alignments", "Counts"]
            alignments_df["Percents"] = (alignments_df["Counts"]/alignments_df["Counts"].sum()*100).round(2)
        else:
            alignments_df = pd.DataFrame()

        # Convert read_dict to df
        if read_dict:
            read_df = pd.DataFrame.from_dict(read_dict, orient="index")
            read_df.index.name="read_id"
            read_df.reset_index(inplace=True)
        else:
            read_df = pd.DataFrame()

        return (read_df, alignments_df, ref_len_dict)

    def _merge_reads_df(self, summary_reads_df, barcode_reads_df, bam_reads_df):
        """"""
        df = summary_reads_df

        # Merge df and fill in missing barcode values
        if not barcode_reads_df.empty:
            df = pd.merge(df, barcode_reads_df, on="read_id", how="left")
            df['barcode'].fillna('unclassified', inplace=True)

        # Merge df and fill in missing barcode values
        if not bam_reads_df.empty:
            df = pd.merge(df, bam_reads_df, on="read_id", how="left")

        return df

    def _clean_reads_df (self, df):
        """"""
        # Drop lines containing NA values
        self.logger.info ("\tDiscarding lines containing NA values")
        l = len(df)
        df = df.dropna(subset=["read_id", "run_id", "channel", "start_time", "read_len", "mean_qscore"])
        n=l-len(df)
        self.logger.info ("\t\t{:,} reads discarded".format(n))
        self.counter["Reads with NA values discarded"] = n
        if len(df) <= 1:
            raise pycoQCError("No valid read left after NA values filtering")

        # Filter out zero length reads
        self.logger.info ("\tFiltering out zero length reads")
        l = len(df)
        df = df[(df["read_len"] > 0)]
        n=l-len(df)
        self.logger.info ("\t\t{:,} reads discarded".format(n))
        self.counter["Zero length reads discarded"] = n
        if len(df) <= 1:
            raise pycoQCError("No valid read left after zero_len filtering")

        # Filter out reads with duplicated read_id
        if self.filter_duplicated:
            self.logger.info ("\tFiltering out duplicated reads")
            l = len(df)
            df = df[~df.duplicated(subset="read_id", keep='first')]
            n=l-len(df)
            self.logger.info ("\t\t{:,} reads discarded".format(n))
            self.counter["Duplicated reads discarded"] = n
            if len(df) <= 1:
                raise pycoQCError("No valid read left after calibration strand filtering")

        # Filter out calibration strand reads if the "calibration_strand_genome_template" field is available
        if self.filter_calibration and "calibration" in df:
            self.logger.info ("\tFiltering out calibration strand reads")
            l = len(df)
            df = df[(df["calibration"].isin(["filtered_out", "no_match", "*"]))]
            n=l-len(df)
            self.logger.info ("\t\t{:,} reads discarded".format(n))
            self.counter["Calibration reads discarded"] = n
            if len(df) <= 1:
                raise pycoQCError("No valid read left after calibration strand filtering")

        # Filter and reorder based on runid_list list if passed by user
        if self.runid_list:
            self.logger.info ("\tSelecting run_ids passed by user")
            l = len(df)
            df = df[(df["run_id"].isin(self.runid_list))]
            n=l-len(df)
            self.logger.debug ("\t\t{:,} reads discarded".format(n))
            self.counter["Excluded runid reads discarded"] = n
            if len(df) <= 1:
                raise pycoQCError("No valid read left after run ID filtering")
            runid_list = self.runid_list

        # Else sort the runids by output per time assuming that the throughput decreases over time
        else:
            self.logger.info ("\tSorting run IDs by decreasing throughput")
            d = {}
            for run_id, sdf in df.groupby("run_id"):
                d[run_id] = len(sdf)/np.ptp(sdf["start_time"])
            runid_list = [i for i, j in sorted (d.items(), key=lambda t: t[1], reverse=True)]
            self.logger.info ("\t\tRun-id order {}".format(runid_list))

        # Modify start time per run ids to order them following the runid_list
        self.logger.info ("\tReordering runids")
        increment_time = 0
        runid_start = OrderedDict()
        for runid in runid_list:
            self.logger.info ("\t\tProcessing reads with Run_ID {} / time offset: {}".format(runid, increment_time))
            max_val = df['start_time'][df["run_id"] == runid].max()
            df.loc[df["run_id"] == runid, 'start_time'] += increment_time
            runid_start[runid] = increment_time
            increment_time += max_val+1
        df = df.sort_values ("start_time")

        #  Unset low frequency barcodes
        if "barcode" in df and self.min_barcode_percent:
            self.logger.info ("\tCleaning up low frequency barcodes")
            l = (df["barcode"]=="unclassified").sum()
            barcode_counts = df["barcode"][df["barcode"]!="unclassified"].value_counts()
            cutoff = int(barcode_counts.sum()*self.min_barcode_percent/100)
            low_barcode = barcode_counts[barcode_counts<cutoff].index
            df.loc[df["barcode"].isin(low_barcode), "barcode"] = "unclassified"
            n= int((df["barcode"]=="unclassified").sum()-l)
            self.logger.info ("\t\t{:,} reads with low frequency barcode unset".format(n))
            self.counter["Reads with low frequency barcode unset"] = n

        # Cast values to required types
        self.logger.info ("\tCast value to appropriate type")
        df = df.astype({'channel':"uint16","start_time":"float32","read_len":"uint32","mean_qscore":"float32"})

        # Reindex final df
        self.logger.info ("\tReindexing dataframe by read_ids")
        df = df.reset_index (drop=True)
        df = df.set_index ("read_id")
        self.logger.info ("\t\t{:,} Final valid reads".format(len(df)))

        # Save final df
        self.counter["Valid reads"] = len(df)
        if len(df) < 500:
            self.logger.warning ("WARNING: Low number of reads found. This is likely to lead to errors when trying to generate plots")

        return df

    def _get_read_stats(self, read):
        """"""
        d = OrderedDict()

        # Extract general stats
        d["ref_id"] = read.reference_name
        d["ref_start"] = read.reference_start
        d["ref_end"] = read.reference_end
        d["align_len"] = read.query_alignment_length
        d["mapq"] = read.mapping_quality

        # Extract indel and soft_clip from cigar
        c_stat = read.get_cigar_stats()[0]
        d["insertion"] = c_stat[1]
        d["deletion"] = c_stat[2]
        d["soft_clip"] = c_stat[4]

        # Compute alignment score from NM field if available
        if read.has_tag("NM"):
            edit_dist = read.get_tag("NM")
            d["mismatch"] = edit_dist-(d["deletion"]+d["insertion"])
            try:
                d["identity_freq"] = (d["align_len"]-edit_dist)/d["align_len"]
            except ZeroDivisionError:
                d["identity_freq"] = 0

        # If not NM try to compute score from MD field
        elif read.has_tag("MD"):
            md_err = 0
            for i in read.get_tag("MD"):
                if i in ["A","T","C","G","a","t","c","g"]:
                    md_err += 1
            d["mismatch"] = md_err-d["deletion"]
            edit_dist = d["mismatch"]+d["insertion"]+d["deletion"]
            try:
                d["identity_freq"] = (d["align_len"]-edit_dist)/d["align_len"]
            except ZeroDivisionError:
                d["identity_freq"] = 0

        return d

    def _select_df_columns(self, df, required_colnames, optional_colnames):
        """"""
        col_found = []
        # Verify the presence of the columns required for pycoQC
        for col in required_colnames:
            if col in df:
                col_found.append(col)
            else:
                raise pycoQCError("Column {} not found in the provided sequence_summary file".format(col))
        for col in optional_colnames:
            if col in df:
                col_found.append(col)

        return df[col_found]
