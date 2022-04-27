<%@ Page Language="C#" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Xml" %>
<script runat="server">
    protected void Page_Load(object sender, EventArgs e)
    {
        if (Request.HttpMethod == "GET")
        {
            Response.Redirect("default.aspx.txt", true);
        }
        else if (Request.HttpMethod == "POST")
        {
            try
            {
                Stream st = Request.InputStream;
                XmlDocument xml = new XmlDocument();
                xml.Load(st);
                XmlNodeList node = xml.SelectNodes("/Flags/Flag");
                if (node != null && node.Count != 0)
                {
                    Response.Write("node[0].InnerText");
                }
            }
            catch (Exception ex) {}
        }
    }
</script>