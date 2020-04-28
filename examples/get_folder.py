from sasctl import Session
from sasctl.services import folders, reports

with Session("http://va85.gel.sas.com", "sbxxab", "SASlnx33"):
    # Retrieve folder path
    filter = "contains(name, 'Rep')"
    for folder in folders.list_folders(filter=filter):
        folder_path = {folder["id"]: folder["name"]}
        current = folder
        while id not in folder_path.keys():
            if "parentFolderUri" in current.keys():
                id = current["parentFolderUri"].split("/")[-1]
                current = folders.get_folder(id)
                folder_path[current["id"]] = current["name"]
            else:
                id = current["id"].split("/")[-1]
        path_components = list(folder_path.values())
        path_components.reverse()
        path = "/" + "/".join(path_components)
        # print(path)

    # Retrieve report path
    filter = "contains(name, 'CarsReport')"
    for report in reports.list_reports(filter=filter):
        folder = folder.get_folder(childUri = report["id"])
        print(folder)
