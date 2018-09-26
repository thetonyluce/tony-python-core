import json
import sys
import urllib.parse


class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        fileinfo = self.filereader()

        # if method is a GET then split path into parts using /
        if method == 'GET':
            split_path = path.split('/')

            # if path is inventory then show inventory
            if split_path[1] == 'inventory' and len(split_path) < 2:
                inventory = json.dumps(fileinfo)
                return inventory

            # else show the inventory of item [2] in the dictionary
            else:
                item = split_path[2]
                if item not in fileinfo:
                    return f"No result. Check inventory with GET http://localhost:8000/inventory."

                else:
                    stock_qty = json.dumps(fileinfo[item])
                    return f"There are {stock_qty} {item} in stock."

        elif method == 'PATCH':
            split_path = path.split('/')  # split the path up in a list
            query_split = query.split('=')  # split the query into a list
            change_in_qty = query_split[1]  # set the change in qty for item
            fileinfo[split_path[2]] = fileinfo[split_path[2]] + int(change_in_qty)  # update qty for path in txt
            self.filewriter(fileinfo)  # write file info to txt file
            return f"{split_path[2]} qty has been updated to {fileinfo[split_path[2]]}"  # give user an update

        elif method == 'POST':
            split_path = path.split('/')  # Split the path up in a list

            if query == "CREATE_ME_PLEASE":  # Test query for DELETE command
                fileinfo[split_path[2]] = 0  # add value to the dictionary
                self.filewriter(fileinfo)  # write file info to txt file
                return f"{split_path[2]} has been added to inventory. Make sure to update the qty."

            else:

                return f"Hey Buddy. Whatcha doin? Envyin my inventory?"

        elif method == 'DELETE':
            split_path = path.split('/')  # Split the path up in a list

            if query == "DELETE_ME_PLEASE":  # Test query for DELETE command
                fileinfo.pop(split_path[2], None)  # Pop the dictionary value out
                self.filewriter(fileinfo)  # write file info to txt file
                return f"{split_path[2]} has been removed from the inventory. Never to return."

            else:

                return f"Oh hey. What's up? Trying to delete stuff, eh?"

    def filewriter(self, fileinfo):
        json.dump(fileinfo, open("inventory_api.txt", 'w'))
        return "Your inventory has been updated."

    def filereader(self):
        _dict = {}
        with open('inventory_api.txt', 'r') as f:
            _dict = json.loads(f.read())
        return _dict
