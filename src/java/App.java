public class App {
	
    public static void main(String[] args) {
        IExplorer proxy = new ProxyExplorer(new Explorer());
        
        proxy.OpenFile("tarea", "PDF");
        proxy.OpenFile("tarea", "TXT");
    }
 }