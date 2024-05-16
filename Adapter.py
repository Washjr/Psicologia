// Classe Cliente
public class Client {
    private Target target;

    public Client(Target target) {
        this.target = target;        
    }

    public void doSomething() {
        target.request();
    }
}

// Interface Alvo
public interface Target {
    public void request();
}

// Classe Adaptador
public class Adapter extends Adaptee implements Target {
    @Override
    public void request(){
        specific_request();
    }    
}

// Classe Adaptada
public class Adaptee {
    public void specific_request(){
         System.out.println("Comportamento específico da solicitação...");
    }    
}
