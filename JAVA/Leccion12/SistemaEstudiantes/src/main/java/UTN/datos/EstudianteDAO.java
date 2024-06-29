package UTN.datos;
import UTN.dominio.Estudiante;
import static UTN.conexion.Conexion.getConnection;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    //metodo listar:
    public List<Estudiante> listar(){
        List<Estudiante> estudiantes = new ArrayList<>();
        //Creamos algunos objetos para comunicarnos a la bd:
        PreparedStatement ps; //preparar la sentencia sql para ejecutar a la bd
        ResultSet rs; //almacena resultado obtenido de la bd
        //creamos objeto conexion:
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes ORDER BY estudiantes2024";
        try{
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2024"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //Lo agregamos a la lista:
                estudiantes.add(estudiante);
            }
        } catch (Exception e){
            System.out.println("Ocurrio un error al seleccionar datos: "+e.getMessage());
        }
        finally {
           try {
                con.close();
           } catch (Exception e){
               System.out.println("Ocurrio un error al cerrar la conexion: "+e.getMessage());
           }
        }//FIN FINALLY
        return estudiantes;
    }// FIN METODO 'LISTAR'
}
