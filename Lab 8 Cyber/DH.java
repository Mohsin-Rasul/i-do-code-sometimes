public class DH {

    public static long power(long a, long b, long p) {
        long res = 1;
        a = a % p;
        
        while (b > 0) {
            if (b % 2 != 0)
                res = (res * a) % p;
            
            b = b >> 1;
            a = (a * a) % p;
        }
        return res;
    }

    public static void main(String[] args) {
        long P = 111; 
        long G = 200;  

        System.out.println("The value of P: " + P);
        System.out.println("The value of G: " + G);

        // --- Alice ---
        long a = 4; 
        System.out.println("The PRIVATE KEY A FOR Alice: " + a);
        
        long x = power(G, a, P); 
        System.out.println("Alice's Public Key (x): " + x);

        // --- Bob ---
        long b = 3; 
        System.out.println("The PRIVATE KEY b FOR Bob: " + b);

        long y = power(G, b, P);
        System.out.println("Bob's Public Key (y): " + y);

        long ka = power(y, a, P);

        long kb = power(x, b, P);

        System.out.println("----------------------------------");
        System.out.println("Secret key for Alice is: " + ka);
        System.out.println("Secret key for Bob is: " + kb);
    }
}