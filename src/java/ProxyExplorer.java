public class ProxyExplorer implements IExplorer{
    public IExplorer explorador;

    public ProxyExplorer(IExplorer exp){
        this.explorador = exp;
    }
    
    @Override
    public void OpenFile(String n, String t){
        this.explorador.OpenFile(n, t);
    }
}
