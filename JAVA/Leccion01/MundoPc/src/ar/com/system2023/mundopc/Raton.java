
package ar.com.system2023.mundopc;

/**
 *
 * @author marianela
 */
public class Raton extends DispositivoEntrada {
    private final int idRaton;
    private static int contadorRatones;
    
    public Raton(String tipoEntrada, String marca){
        super(tipoEntrada, marca);//llamamos a la clase padre con "super"
        this.idRaton = ++Raton.contadorRatones; //para trabajar con "idRaton"
    }

    @Override
    public String toString() {
        return "Raton{" + "idRaton=" + idRaton +", "+super.toString()+ '}';
    }
    
}
