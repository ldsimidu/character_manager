from flask import Flask, jsonify, request, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__, template_folder='my_templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = os.urandom(24)  # Gera uma chave aleatória

# Modelo atualizado com habilidades adicionais
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    character_class = db.Column(db.String(50))
    level = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    strength_modifier = db.Column(db.Integer, default=0)  # Modificador de força
    dexterity = db.Column(db.Integer)
    dexterity_modifier = db.Column(db.Integer, default=0)  # Modificador de destreza
    constitution = db.Column(db.Integer)
    constitution_modifier = db.Column(db.Integer, default=0)  # Modificador de constituição
    intelligence = db.Column(db.Integer)
    intelligence_modifier = db.Column(db.Integer, default=0)  # Modificador de inteligência
    wisdom = db.Column(db.Integer)
    wisdom_modifier = db.Column(db.Integer, default=0)  # Modificador de sabedoria
    charisma = db.Column(db.Integer)
    charisma_modifier = db.Column(db.Integer, default=0)  # Modificador de carisma
    
    acrobatics = db.Column(db.Integer, nullable=False)
    animal_handling = db.Column(db.Integer, nullable=False)
    arcana = db.Column(db.Integer, nullable=False)
    athletics = db.Column(db.Integer, nullable=False)
    deception = db.Column(db.Integer, nullable=False)
    history = db.Column(db.Integer, nullable=False)
    insight = db.Column(db.Integer, nullable=False)
    intimidation = db.Column(db.Integer, nullable=False)
    investigation = db.Column(db.Integer, nullable=False)
    medicine = db.Column(db.Integer, nullable=False)
    nature = db.Column(db.Integer, nullable=False)
    perception = db.Column(db.Integer, nullable=False)
    performance = db.Column(db.Integer, nullable=False)
    persuasion = db.Column(db.Integer, nullable=False)
    religion = db.Column(db.Integer, nullable=False)
    sleight_of_hand = db.Column(db.Integer, nullable=False)
    stealth = db.Column(db.Integer, nullable=False)
    survival = db.Column(db.Integer, nullable=False)
    
    notes = db.Column(db.Text)  # Novo campo para anotações

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/character/<int:character_id>')
def character_details(character_id):
    character = Character.query.get_or_404(character_id)
    return render_template('character_details.html', character=character)

@app.route('/api/characters')
def get_characters():
    characters = Character.query.all()
    return jsonify([{
        'id': char.id,
        'name': char.name,
        'character_class': char.character_class,
        'level': char.level,
        'strength': char.strength,
        'dexterity': char.dexterity,
        'constitution': char.constitution,
        'intelligence': char.intelligence,
        'wisdom': char.wisdom,
        'charisma': char.charisma,
        'acrobatics': char.acrobatics,
        'animal_handling': char.animal_handling,
        'arcana': char.arcana,
        'athletics': char.athletics,
        'deception': char.deception,
        'history': char.history,
        'insight': char.insight,
        'intimidation': char.intimidation,
        'investigation': char.investigation,
        'medicine': char.medicine,
        'nature': char.nature,
        'perception': char.perception,
        'performance': char.performance,
        'persuasion': char.persuasion,
        'religion': char.religion,
        'sleight_of_hand': char.sleight_of_hand,
        'stealth': char.stealth,
        'survival': char.survival,
        'notes': char.notes  # Inclui as anotações na resposta JSON
    } for char in characters])
@app.route('/create_character', methods=['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        try:
            # Recebe os dados como JSON
            data = request.get_json()

            # Cria o personagem a partir dos dados recebidos
            character = Character(
                name=data['name'],
                character_class=data['character_class'],
                level=data['level'],
                strength=data['strength'],
                dexterity=data['dexterity'],
                constitution=data['constitution'],
                intelligence=data['intelligence'],
                wisdom=data['wisdom'],
                charisma=data['charisma'],
                acrobatics=data['acrobatics'],
                animal_handling=data['animal_handling'],
                arcana=data['arcana'],
                athletics=data['athletics'],
                deception=data['deception'],
                history=data['history'],
                insight=data['insight'],
                intimidation=data['intimidation'],
                investigation=data['investigation'],
                medicine=data['medicine'],
                nature=data['nature'],
                perception=data['perception'],
                performance=data['performance'],
                persuasion=data['persuasion'],
                religion=data['religion'],
                sleight_of_hand=data['sleight_of_hand'],
                stealth=data['stealth'],
                survival=data['survival'],
                notes=data.get('notes', '')  # Pega as anotações, caso existam
            )

            # Adiciona o personagem ao banco de dados e comita a transação
            db.session.add(character)
            db.session.commit()

            # Retorna um JSON com uma mensagem de sucesso
            return jsonify({'message': 'Personagem criado com sucesso!'}), 200
        except Exception as e:
            # Retorna um JSON com o erro em caso de falha
            return jsonify({'error': str(e)}), 500

    # Se for GET, renderiza o template de criação
    return render_template('create_character.html')

@app.route('/edit_character/<int:character_id>', methods=['GET', 'POST'])
def edit_character(character_id):
    character = Character.query.get(character_id)
    if request.method == 'POST':
        # Atualizar os atributos principais
        character.name = request.form['name']
        character.character_class = request.form['character_class']
        character.level = request.form['level']
        
        character.strength = request.form.get('strength', type=int)  # Usa get para evitar erro se o campo não existir
        character.dexterity = request.form.get('dexterity', type=int)
        character.constitution = request.form.get('constitution', type=int)
        character.intelligence = request.form.get('intelligence', type=int)
        character.wisdom = request.form.get('wisdom', type=int)
        character.charisma = request.form.get('charisma', type=int)

        # Atualiza os modificadores de habilidade
        character.strength_modifier = request.form.get('strength_modifier', type=int)
        character.dexterity_modifier = request.form.get('dexterity_modifier', type=int)
        character.constitution_modifier = request.form.get('constitution_modifier', type=int)
        character.intelligence_modifier = request.form.get('intelligence_modifier', type=int)
        character.wisdom_modifier = request.form.get('wisdom_modifier', type=int)
        character.charisma_modifier = request.form.get('charisma_modifier', type=int)

        # Atualizar as habilidades
        character.acrobatics = request.form['acrobatics']
        character.animal_handling = request.form['animal_handling']
        character.arcana = request.form['arcana']
        character.athletics = request.form['athletics']
        character.deception = request.form['deception']
        character.history = request.form['history']
        character.insight = request.form['insight']
        character.intimidation = request.form['intimidation']
        character.investigation = request.form['investigation']
        character.medicine = request.form['medicine']
        character.nature = request.form['nature']
        character.perception = request.form['perception']
        character.performance = request.form['performance']
        character.persuasion = request.form['persuasion']
        character.religion = request.form['religion']
        character.sleight_of_hand = request.form['sleight_of_hand']
        character.stealth = request.form['stealth']
        character.survival = request.form['survival']
        
        # Atualizar as anotações
        character.notes = request.form['notes']
        
        # Commit as mudanças
        db.session.commit()
        flash('Character updated successfully!', 'success')
        return redirect(url_for('character_details', character_id=character.id))
    
    return render_template('edit_character.html', character=character)

@app.route('/delete_character/<int:character_id>', methods=['POST'])
def delete_character(character_id):
    character = Character.query.get(character_id)
    if character:
        db.session.delete(character)
        db.session.commit()
        flash('Character deleted successfully!', 'success')
    else:
        flash('Character not found.', 'danger')
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
