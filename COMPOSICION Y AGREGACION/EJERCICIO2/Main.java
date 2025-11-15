package EJERCICIO2;

public class Main {
    public static void main(String[] args) {

        Ropero ropero = new Ropero("Madera");

        ropero.adicionar(new Ropa("Camisa", "Algodón"));
        ropero.adicionar(new Ropa("Polera", "Algodón"));
        ropero.adicionar(new Ropa("Chaqueta", "Cuero"));

        ropero.mostrarPorMaterial("Algodón");
        ropero.eliminarPorMaterial("Algodón");

        ropero.mostrarPorTipo("Chaqueta");
    }
}
