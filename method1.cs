//  Author mounicraju@gmail.com //

using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.Configuration;
using System.Net;
using System.Collections.Generic;

namespace ContentExtractor
// Method 1 //
public void getRobots()
{
    WebClient wClient = new WebClient();
    string url = String.Format("http://{0}/robots.txt", urlBox.Text);

    try
    {
        Stream data = wClient.OpenRead(url);
        StreamReader read = new StreamReader(data);   // defining new stream reader //
        string[] lines = new string[] { read.ReadToEnd() };

        foreach (string line in lines)
        {
            textBox1.AppendText(line + System.Environment.NewLine);
        }
    }
    catch (WebException ex)
    {
        MessageBox.Show(ex.Message, null, MessageBoxButtons.OK);
    }
}
