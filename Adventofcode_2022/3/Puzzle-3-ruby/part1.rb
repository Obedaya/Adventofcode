# frozen_string_literal: true
alphabetlower = ('a'..'z').to_a
alphabetupper = ('A'..'Z').to_a

score = 0

File.open("input-3.txt", "r") do |f|
  f.each_line do |line|
    item = ""
    devidedline = line.chars.each_slice(line.length / 2).map(&:join)
    devidedline[0].each_char do |a|
      devidedline[1].each_char do |b|
        if a == b
          item = a
        end
      end
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

