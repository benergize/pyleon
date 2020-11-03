import json
import sys

def main():

	print("\npyleon 0.1 - Yet more dumb software by Ben Ehrlich (benergize.com)")
	print("Let's Rock and Roll")
	print("----------------------------\n")
	
	if len(sys.argv) < 2:
		print("Please provide the pyleon config file as an argument, or -h for help. Aborting.")
		exit()
	
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print("Use pyleon to combine scripts into a single file. Just create a JSON file in this format (and supply its name as an argument when you run pyleon):\n")
		print('{ "output": "combinedScripts.js", "files": [ "script1.js", "script2.js", "script3.js" ] }')
		print("\nThe scripts will be combined into a single file specified by the output property in the JSON file. The files property specifies what scripts to put together.")
		exit()
		
	shouldImport = sys.argv[1:]
	
		
	
	for f in shouldImport:
	
	
		outputToFile = "pyleon-output"
		master = "";
	
		fo = open(f, "r")
		
		print("Reading " + f + ".")
		goon = False
		
		try:
			obj = json.loads(fo.read())
			goon = True
			
		except (ValueError):
			print("Failed to read JSON. Skipping file.")
			
		if goon:
			if(obj['output']):
				outputToFile = obj['output']
				print("\nWill output to " + outputToFile)
			print("")
			for j in obj['files']:
				
				try:
					print("Reading " + j + ".")
					r2 = open(j,"r")
					master += r2.read()
					r2.close()
				except (e):
					print("Could not read " + j + ".");
			
			fo.close()
		
		try:
			print("\nWriting to " + outputToFile)
			wr = open(outputToFile,"w+")
			wr.write(master)
			wr.close()
			
		except (e):
			print("Could not write to file.")
			
		print("Thanks for playing!")

main()
