public class Client {
    private Target target;

    public Client(Target target) {
        this.target = target;        
    }

    // Código restante...
}

public interface Target {
    public void operation(){
        // Lógica de funcionamento...
    }
}

public class Adapter implements Target extends Adaptee {
    public void operation(){
        specific_operation();
    }    
}

/*
public class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    public void operation(){
        adaptee.specific_operation();
    }
}
*/

public class Adaptee {
    public void specific_operation(){
        // Lógica de funcionamento... 
    }    
}
