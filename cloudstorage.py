from distutils.command.upload import upload
import dropbox 
accesstoken="sl.BHnahMdKzX3cJjXIeW97PQeB1plYNaZGoOey7dwb8ieQ48mpESEXYX_sAnOBGfsB7ucVZHE8AZCt7V5koOKPEh8K9CGpuyLA2cXH1yiNoqRdJixrSj1cqc65jRsW4r5cfLZtIHo_qZ8"
dpx= dropbox.Dropbox(accesstoken)
f=open('file.txt','rb')
dpx.files_upload(f.read(),"/uswa/ppg.txt")
print("file uploaded successfully")