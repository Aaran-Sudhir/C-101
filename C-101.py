#sl.BJajODKMd3ca_GSJMWzFvwuumKZElsjiiPt1Bx7LGC6j90hA0CY7Ad6-bpKGod00xjL3wrgesKkjjxleqSuvecXjjXP0XNC-vmBChOtVI2kleXSkGYwMHrZfIYIcwdeeBiUc0HcLRvMj
import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        with open(fileFrom,'rb') as f:
            dbx.files_upload(f.read(),fileTo)

def main():
    accessToken = 'sl.BJajODKMd3ca_GSJMWzFvwuumKZElsjiiPt1Bx7LGC6j90hA0CY7Ad6-bpKGod00xjL3wrgesKkjjxleqSuvecXjjXP0XNC-vmBChOtVI2kleXSkGYwMHrZfIYIcwdeeBiUc0HcLRvMj'
    transferdata = TransferData(accessToken)
    fileFrom = input("Enter the file you want to taken the backup of")
    fileTo = input("Enter the path where you want to store the backup")
    transferdata.uploadFile(fileFrom,fileTo)
    print("File uploaded")

main()    