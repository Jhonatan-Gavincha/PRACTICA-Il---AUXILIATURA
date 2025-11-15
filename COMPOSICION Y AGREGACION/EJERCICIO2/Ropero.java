package EJERCICIO2;
class Ropero {
    private String material;
    private Ropa[] ropas = new Ropa[20];
    private int nroRopas = 0;

    public Ropero(String material) {
        this.material = material;
    }

    // Adicionar 1 prenda
    public void adicionar(Ropa r) {
        if (nroRopas < 20) {
            ropas[nroRopas] = r;
            nroRopas++;
        } else {
            System.out.println("El ropero está lleno.");
        }
    }

    // Eliminar por material
    public void eliminarPorMaterial(String mat) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equalsIgnoreCase(mat)) {
                for (int j = i; j < nroRopas - 1; j++) {
                    ropas[j] = ropas[j + 1];
                }
                ropas[nroRopas - 1] = null;
                nroRopas--;
                i--;
            }
        }
    }

    // Eliminar por tipo
    public void eliminarPorTipo(String tipo) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getTipo().equalsIgnoreCase(tipo)) {
                for (int j = i; j < nroRopas - 1; j++) {
                    ropas[j] = ropas[j + 1];
                }
                ropas[nroRopas - 1] = null;
                nroRopas--;
                i--;
            }
        }
    }

    // Mostrar por material
    public void mostrarPorMaterial(String mat) {
        System.out.println("Prendas con material '" + mat + "':");
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equalsIgnoreCase(mat)) {
                System.out.println(ropas[i]);
            }
        }
    }

    // Mostrar por tipo
    public void mostrarPorTipo(String tipo) {
        System.out.println("Prendas con tipo '" + tipo + "':");
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getTipo().equalsIgnoreCase(tipo)) {
                System.out.println(ropas[i]);
            }
        }
    }
}
