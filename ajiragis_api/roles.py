from rolepermissions.roles import AbstractUserRole


class Staff(AbstractUserRole):
  available_permissions = {
      'manage_language': True,
      'manage_contribution': True,
  }