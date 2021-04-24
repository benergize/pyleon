var fs = require('fs');

function isset(arg) { return typeof arg != "undefined" && arg != null && arg != ""; }
function print(arg) { return console.log(arg); }

var pyleFile = "";
var argv = process.argv;
var fullFile = "";

print("\npyleon 0.21 - Yet more dumb software by Ben Ehrlich (benergize.com)")
print("Let's Rock and Roll")
print("----------------------------\n")

if(isset(argv[2])) { pyleFile = argv[2]; }
else if(fs.existsSync("pyle.json")) { pyleFile = "pyle.json"; }
else { return print("Please specify a JSON file or create a pyle.json file."); }

if(pyleFile != "") {
    try {

        if(!fs.existsSync(pyleFile)) { throw(`File "${pyleFile}" could not be found.`); }

        print(`Getting configuration from "${pyleFile}"...\n`);

        var data = JSON.parse(fs.readFileSync('pyle.json', 'utf8')); 

        if(!isset(data.files)) { throw (`Please specify the files you want to combine with the "files" property in your JSON file.`); }
        if(!isset(data.output)) { throw (`Please specify the files you want to output to with the "output" property in your JSON file.`); }
        if(!Array.isArray(data.output)) { data.output = [data.output]; }

        data.files.forEach(file=>{

            print(`Reading file "${file}".`);
            let contents = fs.readFileSync(file, 'utf8');
            fullFile += contents;

        });

        print("");

        data.output.forEach(file=>{
            print(` - Writing output to "${file}".`);
            fs.writeFileSync(file, fullFile);
        });

        print("");

        print("Jobs done! Thanks for playing.");

      } catch (err) {
        console.error(err)
      }

}
    
     