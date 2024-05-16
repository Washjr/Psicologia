public class Client {
    private Target target;

    public Client(Target target) {
        this.target = target;        
    }

    // Código restante...
}

public interface Target {
    public void operation();
}

public class Adapter implements Target extends Adaptee {
    @Override
    public void operation(){
        specific_operation();
    }    
}

/*
public class Target {
    public void operation();
}    
*/

/*
public class Adapter extends Target {
    private Adaptee adaptee;

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public void operation(){
        adaptee.specific_operation();
    }
}
*/

public class Adaptee {
    public void specific_operation(){
         // Lógica da operação específica...
    }    
}
