from tinydb import TinyDB
DB = TinyDB("chess_db.json", indent=4, sort_keys=False)


class Report:
    @classmethod
    def sorted_table_by(cls, table: "TinyDB.table", sort_key: str) -> list:
        if sort_key == "score":
            data = sorted(table, key=lambda d: d[sort_key], reverse=True)
        else:
            data = sorted(table, key=lambda d: d[sort_key], reverse=False)
        return data

    @classmethod
    def sorted_list_by(cls, data: list, sort_key: str) -> list:
        if sort_key == "score":
            data = sorted(data, key=lambda d: d[sort_key], reverse=True)
        else:
            data = sorted(data, key=lambda d: d[sort_key], reverse=False)
        return data

    @classmethod
    def sorted_list_by_keys(cls, data: list) -> list:
        data = sorted(data, key=lambda item: (item[0], item[1]), reverse=True)
        return data

    @classmethod
    def sort_duplicated_data(cls, data_list):
        p = 0
        while p < len(data_list):
            duplicated_data = []
            duplicate = 0
            begin = p
            while p < len(data_list) - 1 and data_list[p]["score"] == data_list[p + 1]["score"]:
                duplicated_data.append(data_list[p])
                p += 1
                duplicate += 1
            if len(duplicated_data) > 0:
                duplicated_data.append(data_list[p])
                duplicated_data = Report.sorted_list_by(duplicated_data, "ranking")
                k = 0
                for i in range(begin, begin + duplicate + 1, 1):
                    data_list[i] = duplicated_data[k]
                    k += 1
            p = p + 1
        return data_list
