current_version = input().split('.')
current_version_str = "".join(current_version)
version_update = int(current_version_str) + 1
print('.'.join(str(version_update)))