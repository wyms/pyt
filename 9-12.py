from privileges_and_admin import Admin

# Example usage
admin = Admin("Jane", "Doe", "30", "Female", "New York", ["can add post", "can view private information"])
admin.privileges.show_privileges()
