defmodule Bob do
  def hey(input) do
    cond do
      String.strip(input) == "" -> "Fine. Be that way!"
      String.ends_with?(input, "?") -> "Sure."
      shouting?(input) -> "Whoa, chill out!"
      String.ends_with?(input, "!") -> "Whatever."
      true -> "Whatever."
    end
  end

  def shouting?(input) do
    String.upcase(input) == input and not_just_numbers?(input)
  end

  def not_just_numbers?(input) do
    String.match?(input, ~r/[a-zA-Z]/) or String.match?(input, ~r/[[:alpha:]]/)
  end
end
