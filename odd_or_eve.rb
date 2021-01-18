# in order to get n inputs as input use following code

a = gets.to_i

def iseve(val)
  if (val%2 == 0)
    return "eve"
  elsif (val%2 != 0)
    return "odd"
  else
    return "bruh"
  end
end

(0...a).each do |i|
  puts iseve(gets.to_i)
end

# now print if number is odd or even
