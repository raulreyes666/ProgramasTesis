class Book < ApplicationRecord
    validates :title, presence: true
    validates :author, presence: true
    validates :year, presence: true, numericality: { only_integer: true }
  end