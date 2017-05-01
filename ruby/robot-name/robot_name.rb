class Robot
  def name
    @name ||= christen
  end

  private

  def christen
    "AB142"
  end
end
