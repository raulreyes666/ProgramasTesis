class CreateLibros < ActiveRecord::Migration[8.0]
  def change
    create_table :libros do |t|
      t.string :titulo
      t.string :autor
      t.integer :anio_publicacion

      t.timestamps
    end
  end
end
