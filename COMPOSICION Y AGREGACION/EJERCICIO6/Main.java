package EJERCICIO6;

public class Main {
    public static void main(String[] args) {
        // Crear doctores
        Doctor doc1 = new Doctor("Dr. Pérez", "Cardiología");
        Doctor doc2 = new Doctor("Dra. López", "Pediatría");
        Doctor doc3 = new Doctor("Dr. Gómez", "Neurología");

        // Crear hospitales
        Hospital hosp1 = new Hospital("Hospital Central");
        Hospital hosp2 = new Hospital("Hospital Norte");

        // Asignar doctores a hospitales
        hosp1.asignarDoctor(doc1);
        hosp1.asignarDoctor(doc2);

        hosp2.asignarDoctor(doc2); // doctor puede trabajar en varios hospitales
        hosp2.asignarDoctor(doc3);

        // Mostrar doctores de cada hospital
        hosp1.mostrarDoctores();
        hosp2.mostrarDoctores();
    }
}

