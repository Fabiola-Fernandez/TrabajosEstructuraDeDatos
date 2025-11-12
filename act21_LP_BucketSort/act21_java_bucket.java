import java.util.*;

public class BucketSort {
    public static void bucketSort(float[] arr) {
        int n = arr.length;
        if (n <= 0)
            return;

        @SuppressWarnings("unchecked")
        List<Float>[] buckets = new ArrayList[n];

        for (int i = 0; i < n; i++)
            buckets[i] = new ArrayList<>();

        // Colocar elementos en cubetas
        for (float num : arr) {
            int index = (int) (num * n);
            buckets[index].add(num);
        }

        // Ordenar cada cubeta
        for (int i = 0; i < n; i++)
            Collections.sort(buckets[i]);

        // Unir cubetas
        int idx = 0;
        for (List<Float> bucket : buckets)
            for (float num : bucket)
                arr[idx++] = num;
    }

    public static void main(String[] args) {
        float[] arr = {0.78f, 0.17f, 0.39f, 0.26f, 0.72f, 0.94f, 0.21f, 0.12f, 0.23f, 0.68f};
        bucketSort(arr);

        System.out.println("Arreglo ordenado:");
        for (float num : arr)
            System.out.print(num + " ");
    }
}
