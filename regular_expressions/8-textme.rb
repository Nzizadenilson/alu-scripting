#!/usr/bin/env ruby
matches = ARGV[0].match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
puts "#{matches[1]},#{matches[2]},#{matches[3]}"
