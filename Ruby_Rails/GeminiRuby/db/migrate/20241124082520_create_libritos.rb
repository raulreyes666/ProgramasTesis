class CreateLibritos < ActiveRecord::Migration[8.0]
  def change
    create_table :libritos do |t|
      t.string :title
      t.string :author
      t.integer :year

      t.timestamps
    end
  end
end
