import os

current_user_my_document_folder_path = os.path.join(os.environ["USERPROFILE"], "Documents")
json_file_name = "ApplyOverridesByCategoryParametersCompact"

with open(json_file_name + ".json", "rb") as json_file:
  file_content = json_file.read()

file_bytes_edited = file_content[3:len(file_content)]  # Slice from index 4 to the end
file_bytes_edited = file_bytes_edited.replace(b"\n", b"")  # Replace newline with empty bytes
file_bytes_edited = file_bytes_edited.replace(b"b'", b"")  # Remove b' (not needed for bytes)
file_bytes_edited = file_bytes_edited.replace(b"\r", b"")  # Replace carriage return with empty bytes
file_bytes_edited = file_bytes_edited.replace(b"\t", b"")  # Replace tab with empty bytes
# file_bytes_edited = file_bytes_edited.replace(b" ", b"")  # Replace spaces with empty bytes
file_bytes_edited = file_bytes_edited.replace(b'"', b'\\"')  # Escape double quotes

with open(json_file_name + ".txt", "w") as text_file:
  text_file.write(file_bytes_edited.decode("utf-8"))