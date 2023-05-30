# OpenAI API and Apple II Serial Connection

This is a Python application that allows communication between an Apple II computer and the OpenAI API. The communication is achieved through a tty serial connection.

## Requirements

To use this application, you need the following:

- Python 3.x 
- PySerial
- Requests package
- OpenAI API key
- Apple II computer with a serial port

## Installation

1. Clone the repository to your local machine.
2. Copy the `example.env` file to a new file named `.env`:

```bash
cp example.env .env
```

3. Edit the `.env` file and update the values for the `OPENAIKEY`, `PASSWORD`, and `COMINFO` variables.
   - `OPENAIKEY` should be set to your OpenAI API key.
   - `PASSWORD` should be set to a password of your choice for accessing the application.
   - `COMINFO` should be updated to match the serial port settings for your Apple II computer. The default value is `COM4` for Windows, but you may need to update this value for a Linux system.

```bash
OPENAIKEY=your_api_key_here
PASSWORD=your_password_here
COMINFO=your_com_info_here
```

4. Connect your Apple II computer to your machine via a serial cable.
5. Start the Python program by running the following command:

```bash
python3 openai_apple.py
```
6. Here you will need a terminal software application for Apple ][, Apple IIe, Apple IIc or Apple IIGS. I personally use [ANSITerm](https://www.whatisthe2gs.apple2.org.za/ansiterm-v2-1.html) on GS-OS and [AGATE](https://archive.org/details/009_Agate_Version_089_ProDOS_Version) on Apple II from a 5 inch floppy. Once you're in, depending on your software choose the setting to match the settings in the iiAI.py code:
```bash
baudrate=9600,
bytesize=8,
timeout=2,
stopbits=serial.STOPBITS_ONE,
parity=serial.PARITY_EVEN 
```
7. The terminal screen will prompt you to enter a username and password. Please note that the user running the Python code will be the host user for the machine and enter the password you set in step 3.
8. After entering the correct credentials, the introduction message will be displayed, and the application will be ready to receive input. 



## Usage

1. Start the Python program by running the following command:

```bash
python3 iiAI.py
```
2. The terminal screen will prompt you to enter a username and password. Use any username you like, and enter the password you set in step 3.
3. After entering the correct credentials, the introduction message will be displayed, and the application will be ready to receive input. 

4. The terminal screen will display an introduction message followed by a prompt:

```
Hostname: <your_hostname>
Local Time: <current_time>
IP Address: <your_ip_address>
Username: <your_username>

openai>
```

5. The prompt indicates that the application is ready to receive input. To send a message to the OpenAI API, type your message after the prompt (i.e., "openai>"), and press "Enter." The program will send your message to the API and return the response.

6. If you type a command that begins with "!", the program will execute the command in a shell. For instance, if you type "!ls", the program will execute the "ls" command in a shell and display the output.

7. To exit the program, send the exit command:

```bash
exit
```

Note: If you are prompted to enter a username and password, use the username and password provided in the `.env` file.

## Contributing

If you want to contribute to this project, please follow the below steps:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

This project was inspired by the following resources:

- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Python Serial Communication Tutorial](https://pyserial.readthedocs.io/en/latest/shortintro.html)

## Donate

I hope you found my work useful and it has helped you in some way. As an independent developer, I have put a lot of time and effort into creating this project. If you appreciated my work and would like to support me, please consider making a donation.

Your contribution will help me to continue improving and expanding this project, as well as creating new ones in the future. Any amount, no matter how small, is deeply appreciated.

Thank you for your support!

Donate here: https://ko-fi.com/fiskarwhiskers