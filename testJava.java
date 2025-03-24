public class testJava {
	public static void main(String[] args) {
	 long sum = 0;
        long start = System.currentTimeMillis();
        for (long i = 0; i < 1_000_000L; i++) {
            sum += i * i;
        }
        long diff = System.currentTimeMillis() - start;
        System.out.println(diff + "ms");
	}
}