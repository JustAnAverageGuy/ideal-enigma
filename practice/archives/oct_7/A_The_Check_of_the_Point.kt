fun pointLocation(x: Int, y: Int, a: Int): String {
    // Coordinates of the square's corners
    val x1 = 0.0
    val y1 = 0.0
    val x2 = a
    val y2 = a
    
    // Check if the point is inside, on the side, or outside the square
    if (x > x1 && x < x2 && y > y1 && y < y2) {
        return "0"
    } else if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
        return "1"
    } else {
        return "2"
    }
}



fun main() {
    val input = readLine()
    
    if (input != null) {
        val integers = input.split(" ").map { it.toIntOrNull() }
        
        if (integers.size == 3 && integers.all { it != null }) {
            val (a, x, y) = integers.mapNotNull { it }
            println(pointLocation(x,y,a))
        } else {
            println("Invalid input. Please enter three integers separated by spaces.")
        }
    } else {
        println("Input is null.")
    }
}
/*

⠀⠀⢀⣤⣶⣶⣤⣄⡀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠸⣿⣿⣿⣿⣿⡟⡟⡗ ⣿⠉⣿⠉⣿⡏⠹⡏⢹⡏⢹⣿⣿⠉⣿⠉⣿⡟⢋⠛⣿⠉⡟⢉⡏⠹⠏⣹⣿
⠀⠀⠙⠏⠯⠛⣉⢲⣧⠟ ⣿⠄⣿⠄⣿⡇⡄⠁⢸⡇⢸⣿⣿⠄⣿⠄⣿⠄⣿⣿⣿⠄⡀⢻⣿⡄⢠⣿⣿
⠀⠀⠠⢭⣝⣾⠿⣴⣿⠇ ⣿⣦⣤⣴⣿⣧⣿⣤⣼⣧⣬⣭⣿⣦⣤⣴⣿⣧⣤⣤⣿⣤⣷⣤⣿⣧⣼⣿⣿
⠀⠀⢐⣺⡿⠁⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣶⣶⣶⣶⣶⣶⠀
⠀⠀⣚⣿⠃ ⣶⣶⣶⣶
⢀⣿⣿⣿⣷⢒⣢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣶⣄⠄
⢰⣿⣿⡿⣿⣦⠬⢝⡄⠀⠀⠀⠀⠀⠀⢠⣿⠿⠿⠟⠛⠋⠁
⠠⢿⣿⣷⠺⣿⣗⠒⠜⡄⠀⠀⠀⠀⣴⠟⠁
⠀⣰⣿⣷⣍⡛⣯⣯⣙⡁⠀⠀⣠⡾⠁
⠀⠨⢽⣿⣷⢍⣛⣶⢷⣼⣠⣾⠋
⠀⠀⠘⢿⣿⣖⠬⣹⣶⣿⠟⠁
⠀⠀⠀⠚⠿⠿⡒⠨⠛⠋
⠀⠀⠀⠐⢒⣛⣷
⠀⠀⠀⢘⣻⣭⣭
⠀⠀⠀⡰⢚⣺⣿
⠀⠀⢠⣿⣿⣿⣿⣦⡄
⠀⠀⢸⡿⢿⣿⢿⡿⠃
⠀⠀⠘⡇⣸⣿⣿⣿⣆
⠀⠀⠀⠀⠸⣿⡿⠉⠁
⠀⠀⠀⠀⠀⢿⡟

*/