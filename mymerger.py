import os
def mergefiles(file_list,output_file):
	f_out = file(output_file,'w')
	tot=0
	for f in file_list:
		f_in = file(f)
		tot=tot+int(f_in.read())
		f_in.close()
	f_out.write(str(tot))
	f_out.flush()
	f_out.close()
	return True