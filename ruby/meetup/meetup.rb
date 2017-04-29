require 'date'

# Determine's a meetup day from a year, month, day, and vague week.
class Meetup
  class InvalidDay < RuntimeError; end

  MONTH_INTERVALS = {
    teenth: 13,
    first: 1,
    second: 8,
    third: 15,
    fourth: 22,
    fifth: 29,
    last: 25,
    feb_last: 23
  }.freeze

  def initialize(month, year)
    @month = month
    @year = year
  end

  def day(weekday, week)
    week = :feb_last if last_week_of_february?(week)
    initial = Date.new(@year, @month, MONTH_INTERVALS[week])
    match_day(initial, weekday)
  rescue
    raise InvalidDay('Oh, what a day.')
  end

  private

  def last_week_of_february?(week)
    @month == 2 && week == :last
  end

  def match_day(initial_date, weekday)
    return initial_date if initial_date.send(weekday.to_s + '?')
    match_day(initial_date.next, weekday)
  end
end
