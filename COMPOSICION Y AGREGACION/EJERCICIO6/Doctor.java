package EJERCICIO6;
import java.util.ArrayList;
import java.util.List;

// Clase Doctor
class Doctor {
    private String nombre;
    private String especialidad;

    public Doctor(String nombre, String especialidad) {
        this.nombre = nombre;
        this.especialidad = especialidad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEspecialidad() {
        return especialidad;
    }

    @Override
    public String toString() {
        return nombre + " - " + especialidad;
    }
}

// Clase Hospital
class Hospital {
    private String nombre;
    private List<Doctor> doctores;

    public Hospital(String nombre) {
        this.nombre = nombre;
        this.doctores = new ArrayList<>();
    }

    // Asignar doctor (agregación)
    public void asignarDoctor(Doctor doctor) {
        if (!doctores.contains(doctor)) {
            doctores.add(doctor);
        }
    }

    // Mostrar doctores
    public void mostrarDoctores() {
        System.out.println("Doctores en " + nombre + ":");
        for (Doctor doc : doctores) {
            System.out.println(" - " + doc);
        }
    }
}