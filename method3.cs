// Author  mounicraju@gmail.com //

using .Read() in a while loop instead of .ReadToEnd()
Debug and check the count of lines[] to verify this.


// Method 3 //

Stream data = wClient.OpenRead(url);
StreamReader read = new StreamReader(data);

List<string> lines = new List<string>();

string nextLine = read.ReadLine();  
while (nextLine != null)
{
    lines.Add(nextLine);
    nextLine = read.ReadLine();
}

textBox1.Lines = lines.ToArray();
