public class Explorer implements IExplorer{
    
    @Override
    public void OpenFile(String n, String t){
        if (t == "PDF")
        {
            new PDF(n).AbrirArchivo();
            return;
        }
        new TXT(n).AbrirArchivo();
    }
}
