# frozen_string_literal: true

alphabetlower = ('a'..'z').to_a
alphabetupper = ('A'..'Z').to_a

score = 0

def comparelines(rucksack)
  rucksack[0].each_char do |a|
    rucksack[1].each_char do |b|
      rucksack[2].each_char do |c|
        if a == b && b == c
          return a
        end
      end
    end
  end
end

File.open("input-3.txt", "r") do |f|
  rucksack = []
  i = 0
  f.each_line do |line|
    item = ""
    rucksack[i] = line

    if i == 2
      item = comparelines(rucksack)
      rucksack.clear
      i = 0
    else
      i += 1
    end

    if alphabetlower.include? item
      score += alphabetlower.index(item) + 1
    else if alphabetupper.include? item
      score += alphabetupper.index(item) + 27
         end
    end
  end
  print score
end

