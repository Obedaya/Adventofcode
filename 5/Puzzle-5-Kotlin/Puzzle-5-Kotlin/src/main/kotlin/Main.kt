import java.io.File

fun readFileAsLinesUsingReadLines(fileName: String): List<String>
        = File(fileName).readLines()

fun twoPair(list1: MutableList<String>, list2: MutableList<String>): Pair<MutableList<String>,MutableList<String>> = list1 to list2

fun isNumeric(toCheck: String): Boolean {
    return toCheck.toDoubleOrNull() != null
}

fun createArrayFromInput(file: List<String>,index: Int): MutableList<String> {
    val array: MutableList<String> = mutableListOf()
    var indexRow = 0

    //Find Row of Index
    for (j in file[file.lastIndex]){
        if (j.isDigit() && j.digitToInt() == index){
            indexRow = file[file.lastIndex].indexOf(index.toString()) + 1
            break
        }
    }

    //For Loop Columns
    for (i in 0..(file.lastIndex-1)){
        array.add(file[i].substring(indexRow-1,indexRow))
    }
    return array
}

fun move(steps: List<Int>,container1: MutableList<String>, container2: MutableList<String>) :Pair<MutableList<String>,MutableList<String>>{
    if (steps[0] > 1){
        for(i in steps[0]..0){
            container2.add(container1[0])
            container1.removeAt(0)
        }
    }
    else{
        container2.add(container1[0])
        container1.removeAt(0)
    }
    return twoPair(container1,container2)
}

fun main() {
    val instructions = readFileAsLinesUsingReadLines("src/main/kotlin/input5.txt")
    val start = readFileAsLinesUsingReadLines("src/main/kotlin/input5-start.txt")

    var c1 = createArrayFromInput(start, 1)
    var c2 = createArrayFromInput(start, 2)
    var c3 = createArrayFromInput(start, 3)
    var c4 = createArrayFromInput(start, 4)
    var c5 = createArrayFromInput(start, 5)
    var c6 = createArrayFromInput(start, 6)
    var c7 = createArrayFromInput(start, 7)
    var c8 = createArrayFromInput(start, 8)
    var c9 = createArrayFromInput(start, 9)

    var containerlist = arrayOf(c1,c2,c3,c4,c5,c6,c7,c8,c9)


    for (i in instructions.indices){
        var steps: MutableList<Int> = mutableListOf()

        for (j in instructions[i]) {
            if (j.isDigit() && isNumeric(instructions[i].substring(j.digitToInt()-1,j.digitToInt()))){
                steps.add(j.plus(instructions[i].substring(j.digitToInt()-1,j.digitToInt())).toInt())
            }
        }
        val (container1,container2) = move(steps, containerlist[steps[1]-1], containerlist[steps[2]-1])
        containerlist[steps[1]-1] = container1
        containerlist[steps[2]-1] = container2
    }
    println(containerlist)
}