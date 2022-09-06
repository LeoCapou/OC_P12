from rest_framework import permissions


class Access_Client(permissions.BasePermission):
    """
    Autorise l'accès au client à tous les sales contact + tous les support contact
    Autorise accès/modification du client au sales contact responsable de ce client
    """

    def has_permission(self, request, view):
        return request.user.is_sales or request.user.is_support

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact.user:  # sales contact du client
            return True
        elif (
            request.user.is_sales or request.user.is_support
        ):  # autre sales/support contact (lecture seule)
            if request.method == "PUT" or request.method == "DELETE":
                return False
            else:
                return True
        return False


class Access_Contrat(permissions.BasePermission):
    """
    Autorise l'accès au contrat à tous les sales contact + tous les support contact
    Autorise accès/modification du client au sales contact responsable de ce client
    """

    def has_permission(self, request, view):
        return request.user.is_sales or request.user.is_support

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact.user:  # sales contact du contrat
            return True
        elif (
            request.user.is_sales or request.user.is_support
        ):  # autre sales/support contact (lecture seule)
            if request.method == "PUT" or request.method == "DELETE":
                return False
            else:
                return True
        return False


class Access_Event(permissions.BasePermission):
    """
    Autorise l'accès à l'event à tous les sales contact + tous les support contact
    Autorise accès/modification de l'event aux sales contact + support contact responsable de l'event
    """

    def has_permission(self, request, view):
        return request.user.is_sales or request.user.is_support

    def has_object_permission(self, request, view, obj):
        if (
            request.user == obj.sales_contact.user
            or request.user == obj.support_contact.user
        ):  # sales/support contact du contrat
            return True
        elif (
            request.user.is_sales or request.user.is_support
        ):  # autre sales/support contact (lecture seule)
            if request.method == "PUT" or request.method == "DELETE":
                return False
            else:
                return True
        return False
