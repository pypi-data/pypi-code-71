from tktl.commands.health import GetGrpcHealthCommand, GetRestHealthCommand


def test_health(logged_in_context, test_user_deployed_repos):
    for repo, branch, endpoint in test_user_deployed_repos[2:]:
        cmd = GetRestHealthCommand(
            repository=repo, branch_name=branch, local=False, health_check=True
        )
        result = cmd.execute()
        assert result.status_code == 200

    grpc_repo_name, grpc_repo_branch, grpc_repo_endpoint = test_user_deployed_repos[-1]
    cmd = GetGrpcHealthCommand(
        repository=grpc_repo_name,
        branch_name=grpc_repo_branch,
        local=False,
        health_check=True,
    )
    result = cmd.execute()
    assert result is True
