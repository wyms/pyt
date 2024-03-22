def create_data_dictionary(object_metadata):
  """
  This function takes Salesforce object metadata and creates a data dictionary.

  Args:
      object_metadata (dict): A dictionary containing Salesforce object metadata.

  Returns:
      dict: A dictionary containing the data dictionary.
  """
  data_dictionary = {}
  fields = object_metadata.get('fields', [])

  for field in fields:
    field_dict = {}
    field_dict['name'] = field.get('name')
    field_dict['type'] = field.get('type')
    field_dict['label'] = field.get('label')
    # Add additional properties as needed (e.g., picklist values, length)
    data_dictionary[field_dict['name']] = field_dict

  return data_dictionary

# Example Usage (replace with actual object metadata)
object_metadata = {
  
  "name": "Account",
  "fields": [
    {"name": "Name", "type": "string", "label": "Account Name"},
    {"name": "Industry", "type": "picklist", "label": "Industry"}
  ]
}

data_dictionary = create_data_dictionary(object_metadata)
print(data_dictionary)