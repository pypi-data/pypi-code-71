# THIS FILE IS AUTO-GENERATED. DO NOT EDIT
from verta._swagger.base_type import BaseType

class ModeldbHydratedProject(BaseType):
  def __init__(self, project=None, collaborator_user_infos=None, owner_user_info=None, allowed_actions=None):
    required = {
      "project": False,
      "collaborator_user_infos": False,
      "owner_user_info": False,
      "allowed_actions": False,
    }
    self.project = project
    self.collaborator_user_infos = collaborator_user_infos
    self.owner_user_info = owner_user_info
    self.allowed_actions = allowed_actions

    for k, v in required.items():
      if self[k] is None and v:
        raise ValueError('attribute {} is required'.format(k))

  @staticmethod
  def from_json(d):
    from .ModeldbProject import ModeldbProject

    from .ModeldbCollaboratorUserInfo import ModeldbCollaboratorUserInfo

    from .UacUserInfo import UacUserInfo

    from .UacAction import UacAction


    tmp = d.get('project', None)
    if tmp is not None:
      d['project'] = ModeldbProject.from_json(tmp)
    tmp = d.get('collaborator_user_infos', None)
    if tmp is not None:
      d['collaborator_user_infos'] = [ModeldbCollaboratorUserInfo.from_json(tmp) for tmp in tmp]
    tmp = d.get('owner_user_info', None)
    if tmp is not None:
      d['owner_user_info'] = UacUserInfo.from_json(tmp)
    tmp = d.get('allowed_actions', None)
    if tmp is not None:
      d['allowed_actions'] = [UacAction.from_json(tmp) for tmp in tmp]

    return ModeldbHydratedProject(**d)
