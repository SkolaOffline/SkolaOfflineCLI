# SkolaOffline-CLI
SkolaOffline is our project which is an unnoficial client for Skola Online. This is the command line interface for the project written in python. The program uses the default endpoint https://aplikace.skolaonline.cz/ so we are sorry for the students from Plzeň.  We decided to write the cli in order to figure out what is necessary for the full version [coming soon™](https://github.com/SkolaOffline/skolaoffline). 

## Installation
To install the cli, you need to have python installed on your computer. You can download the latest version of python [here](https://www.python.org/downloads/). After you have installed python, download the zip file from github and extract it. Open a terminal in the folder where you extracted the files and run the following command:

```pip install -r "_Path_to_requirements.txt"```

This will install the required dependecies for the cli. You can of course install the packages to a venv if you want to keep your system clean. After you have installed the dependencies, you can start using the cli.

## Usage
Before you can use the cli, you need to save your credentials. In order to get your credentials you need to have an account at [Skola Online](https://www.skolaonline.cz/). The access to this system is provided by your school. You can login by creating a file called ```credentials``` without any file extension in the same folder as the cli. The file should contain the following
    
```
Your_Username
Your_Password
```

This will get the access and refresh tokens automatically whenever the request fails and save them in a file called token. If you logged in previously, you can skip this step and the cli should try to login automatically using the refresh token. The credentials file is highly encouraged because if you login on another device, the refresh token is deemend invalid by the server and you need to login again.

After you have logged in, you can start using the cli by appending the arguments to the command ```.\main.py```. The available commands are listed below.

| Command   | Arguments            | Description                                                                                                                                                                   |
|-----------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Help      | --help or -h      | Shows you a brief help menu similar to this with all available commands.                                                                                                      |
| Timetable | --timetable or -t | Shows a timetable for the present week or following week if it is weekend.  The timetable is shown in a table.                                                                |
| Marks     | --marks or -m     | Shows marks for each subject in a table with averages.  Shows marks for the current semester.                                                                                 |
| Absences  | --absences or -a  | Shows your absences in three tables.  First is a table of absences by the dates. Second shows absences in subjects. Third is total absences. All are in the present semester. |
| Messages  | --messages or -z  | Shows a brief table of messages with index numbers.  If you want to see a text of a message use method bellow.                                                                |
| Message   | --message <index_number> or -k <index_number>  | Shows the message with content based on the index number obtained in method above.                                                                                            |
| Report    | --report or -r    | Shows all of your reports from each semester.                                                                                                                                 |                                                                                                                        |

You can have a look at the available commands in the program using 
    
```.\main.py --help``` or ```.\main.py -h```



## Contributing
If you want to contribute to the project, you can fork the repository and make a pull request. We will review the pull request and merge it if it is good.

## License
DSMS license - don't snatch my stuff license

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
