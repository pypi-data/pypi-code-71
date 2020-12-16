# utility_views.py
#
#   These are views that are used for common tasks
#

from django.http import JsonResponse
from psu_base.classes.Log import Log
from psu_base.classes.ConvenientDate import ConvenientDate
from psu_base.classes.DynamicRole import DynamicRole
from datetime import date
from psu_base.services import error_service, banner_service, utility_service

log = Log()
allowable_role_list = DynamicRole().super_user()


def banner_menu_options(request, menu_type):
    """
    Get menu options from Banner validation tables.
    Examples of menu_type include state, nation, race, ethnicity, ...
    The complete list of available menu_types is only found in Banner: api/dbprocs/zwd_form_options
    """
    return banner_service.finti_get_menu_options_response(menu_type)


def validate_date_format(request):
    """
    Given a date input, validate the date format and return in standard format, or Forbidden if invalid

    Params:
        date_string:    The date entered by the user

        Optional:
            response_type:  { date, datetime } (defaults to 'date')
            min_years:      Minimum acceptable age of given date in years
            max_years:      Maximum acceptable age of given date in years
            min_days:      Minimum acceptable age of given date in days
            max_days:      Maximum acceptable age of given date in days
    """
    date_string = request.GET.get('date_string')
    log.trace([date_string])

    data = {
        'given': date_string,
        'converted_date': None,
        'converted_datetime': None,
        'age_days': None,
        'age_years': None,
        'error_message': None
    }

    try:
        if not date_string:
            data['error_message'] = "No date was given"
            response = JsonResponse(data)
            response.status_code = 403
            return response

        else:
            date_cd = ConvenientDate(date_string)

            if date_cd.conversion_error:
                data['error_message'] = date_cd.conversion_error
                response = JsonResponse(data)
                response.status_code = 403
                return response

            elif not date_cd.datetime_instance:
                data['error_message'] = "Could not recognize the given date format"
                response = JsonResponse(data)
                response.status_code = 403
                return response

            # Convert to standard date and datetime strings
            data['converted_date'] = date_cd.date_field()
            data['converted_datetime'] = date_cd.timestamp()

            # Prepare to calculate age
            given_datetime = date_cd.datetime_instance
            given_date = date(given_datetime.year, given_datetime.month, given_datetime.day)
            today = date.today()

            # Get age in years (negative age indicates future date)
            age = today.year - given_date.year - ((today.month, today.day) < (given_date.month, given_date.day))
            data['age_years'] = age

            # Get age in days (negative age indicates future date)
            delta = today - given_date
            data['age_days'] = delta.days

            return JsonResponse(data)

    except Exception as ee:
        data['error_message'] = f"Invalid date: {date_string}"
        response = JsonResponse(data)
        response.status_code = 403
        return response


def format_phone_number(request):

    phone_string = request.GET.get('phone_number')
    log.trace([phone_string])

    data = {
        'given': phone_string,
        'converted': phone_string,
        'phone_digits': None,
        'phone_length': 0,
    }

    try:
        data['converted'] = utility_service.format_phone(phone_string)
        data['phone_digits'] = utility_service.format_phone(phone_string, True)
        data['phone_length'] = len(data['phone_digits'])
        response = JsonResponse(data)
    except Exception as ee:
        response = JsonResponse(data)
        response.status_code = 403
        error_service.record(ee, phone_string)

    return response
