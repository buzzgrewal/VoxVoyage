import os
import gradio as gr
import torch
import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict

device = "cuda" if torch.cuda.is_available() else "cpu"
model = Zonos.from_pretrained("Zyphra/Zonos-v0.1-transformer", device=device)

story = {
    "start": {
        "text": (
            "You wake up in a mysterious forest. The air is cool and the silence is eerie. "
            "Shadows dance between ancient trees, and you feel as if unseen eyes are watching your every move."
        ),
        "emotion": "anxious",
        "options": [
            {"choice": "Follow the narrow path", "next": "path"},
            {"choice": "Venture off into the trees", "next": "trees"}
        ]
    },
    "path": {
        "text": (
            "You follow the narrow, winding path. As you proceed, the rustling leaves and distant creaks "
            "fill you with a growing sense of unease. Ahead, a dim light flickers in the distance."
        ),
        "emotion": "cautious",
        "options": [
            {"choice": "Investigate the light", "next": "cottage"},
            {"choice": "Keep following the path", "next": "continue_path"}
        ]
    },
    "trees": {
        "text": (
            "Disregarding the path, you dive deeper into the thick trees. A haunting melody weaves through the air, "
            "pulling you further from safety into a realm of shadows."
        ),
        "emotion": "uneasy",
        "options": [
            {"choice": "Follow the melody", "next": "melody"},
            {"choice": "Turn back toward the path", "next": "path"}
        ]
    },
    "cottage": {
        "text": (
            "You approach a quaint, weathered cottage with flickering candlelight in the window. An elderly woman "
            "stands at the door, her eyes both inviting and sorrowful."
        ),
        "emotion": "mysterious",
        "options": [
            {"choice": "Enter the cottage", "next": "stories"},
            {"choice": "Politely decline and leave", "next": "decline"}
        ]
    },
    "continue_path": {
        "text": (
            "You continue along the path, which now forks into two. One branch is overgrown and wild, while the "
            "other is disturbingly clear, as if recently traveled."
        ),
        "emotion": "apprehensive",
        "options": [
            {"choice": "Take the overgrown branch", "next": "abandoned_village"},
            {"choice": "Take the clear branch", "next": "hidden_cave"}
        ]
    },
    "melody": {
        "text": (
            "The melody leads you to a clearing where an ancient shrine looms. The air is thick with secrets, and "
            "a spectral figure lingers at the edge of your vision."
        ),
        "emotion": "haunted",
        "options": [
            {"choice": "Approach the shrine", "next": "haunted_shrine"},
            {"choice": "Confront the spectral figure", "next": "mysterious_figure"}
        ]
    },
    "stories": {
        "text": (
            "Inside the cottage, the elderly woman recounts tales of lost souls and forgotten curses that haunt this forest. "
            "Her words reveal clues of a hidden terror lurking in the shadows."
        ),
        "emotion": "foreboding",
        "options": [
            {"choice": "Investigate further based on her clues", "next": "secret_revelation"},
            {"choice": "Leave the cottage in fear", "next": "decline"}
        ]
    },
    "decline": {
        "text": (
            "You decide not to trust the ominous signs. As you step away, the forest seems to close in around you, "
            "and you realize you may have lost your way."
        ),
        "emotion": "desperate",
        "options": [
            {"choice": "Try to find a way out", "next": "lost_in_darkness"},
            {"choice": "Return to the path", "next": "path"}
        ]
    },
    "left_fork": {
        "text": (
            "You take the left fork, and the forest darkens unnaturally. Every rustle and whisper sends shivers down your spine, "
            "as if something sinister stalks your every step."
        ),
        "emotion": "terrified",
        "options": [
            {"choice": "Press on despite the fear", "next": "sinister_shadow"},
            {"choice": "Turn back immediately", "next": "decline"}
        ]
    },
    "right_fork": {
        "text": (
            "You choose the right fork, where the trees part to reveal a brief, clear sky. Yet, a feeling of false hope fills you; "
            "the calm appears too contrived."
        ),
        "emotion": "suspicious",
        "options": [
            {"choice": "Investigate the clearing", "next": "final_escape"},
            {"choice": "Ignore it and continue", "next": "left_fork"}
        ]
    },
    "abandoned_village": {
        "text": (
            "The overgrown branch leads you to the ruins of an abandoned village. Crumbling houses and faded relics whisper of a tragic past, "
            "while an eerie silence pervades the area."
        ),
        "emotion": "somber",
        "options": [
            {"choice": "Search the village for clues", "next": "secret_revelation"},
            {"choice": "Quickly leave the village", "next": "continue_path"}
        ]
    },
    "hidden_cave": {
        "text": (
            "Taking the clear branch, you discover a hidden cave entrance veiled by ivy. A cold breeze from within hints at "
            "frozen memories and long-forgotten terrors."
        ),
        "emotion": "curious",
        "options": [
            {"choice": "Enter the cave", "next": "final_confrontation"},
            {"choice": "Retreat and take the other branch", "next": "abandoned_village"}
        ]
    },
    "haunted_shrine": {
        "text": (
            "At the shrine, ghostly chants echo amid the still air. An altar, adorned with cryptic symbols and withered offerings, "
            "implies that disturbing forces are at work."
        ),
        "emotion": "ominous",
        "options": [
            {"choice": "Attempt to decipher the symbols", "next": "secret_revelation"},
            {"choice": "Flee the shrine immediately", "next": "decline"}
        ]
    },
    "mysterious_figure": {
        "text": (
            "The spectral figure approaches, its face shrouded in mist. It gestures silently as if pleading for help, yet its eyes "
            "reveal centuries of sorrow and warning."
        ),
        "emotion": "melancholic",
        "options": [
            {"choice": "Follow the figure", "next": "secret_revelation"},
            {"choice": "Resist and run away", "next": "lost_in_darkness"}
        ]
    },
    "secret_revelation": {
        "text": (
            "Piecing together the clues, you uncover a horrifying secret: the forest is a nexus of restless spirits, bound by an "
            "ancient, malevolent curse. The revelation sends chills coursing through your veins."
        ),
        "emotion": "shocked",
        "options": [
            {"choice": "Decide to break the curse", "next": "final_confrontation"},
            {"choice": "Flee in terror", "next": "lost_in_darkness"}
        ]
    },
    "lost_in_darkness": {
        "text": (
            "You wander aimlessly as the forest transforms into a labyrinth of twisting paths and suffocating darkness. Every step "
            "feels like a descent into madness."
        ),
        "emotion": "panic",
        "options": [
            {"choice": "Try to recall the clues from earlier", "next": "secret_revelation"},
            {"choice": "Surrender to despair", "next": "decline"}
        ]
    },
    "sinister_shadow": {
        "text": (
            "As you press on, a sinister shadow materializes behind you, growing larger and more menacing with every heartbeat. "
            "Its overwhelming presence leaves you paralyzed with fear."
        ),
        "emotion": "horrified",
        "options": [
            {"choice": "Stand your ground and confront it", "next": "final_confrontation"},
            {"choice": "Run as fast as you can", "next": "lost_in_darkness"}
        ]
    },
    "final_escape": {
        "text": (
            "In a desperate bid for freedom, you dash toward the clearing. The forest seems to part before you, offering a fleeting "
            "escape from the encroaching terror."
        ),
        "emotion": "relieved",
        "options": [
            {"choice": "Run without looking back", "next": "final_confrontation"},
            {"choice": "Slow down and search for any signs of help", "next": "secret_revelation"}
        ]
    },
    "final_confrontation": {
        "text": (
            "The moment of truth arrives as you confront the malevolent force head-on. In the heart of the cursed forest, "
            "a fierce battle of wills ensues—your very soul hangs in the balance."
        ),
        "emotion": "determined",
        "options": [
            {"choice": "Use the power of your revelation to break the curse", "next": "final_escape"},
            {"choice": "Succumb to the darkness", "next": "lost_in_darkness"}
        ]
    }
}


import math
import os
import torchaudio.sox_effects as sox_effects

def generate_tts_audio(text, voice_sample_path, emotion="neutral", language="en-us",
                       speaking_rate=1.0, pitch=1.0):


    print(f"Generating TTS audio for text: {text}")
    wav, sr = torchaudio.load(voice_sample_path)
    speaker = model.make_speaker_embedding(wav, sr)

    cond_dict = make_cond_dict(
        text=text,
        speaker=speaker,
        language=language
    )

    conditioning = model.prepare_conditioning(cond_dict)
    codes = model.generate(conditioning)
    wavs = model.autoencoder.decode(codes).cpu()

    effects = []
    if speaking_rate != 1.0:
        effects.append(["tempo", str(speaking_rate)])
    if pitch != 1.0:
        semitones = 12 * math.log2(pitch)
        effects.append(["pitch", f"{semitones:.2f}"])
        effects.append(["rate", str(sr)])

    if effects:
        wavs_transformed, _ = sox_effects.apply_effects_tensor(wavs[0].unsqueeze(0), sr, effects)
        wav_final = wavs_transformed.squeeze(0)
    else:
        wav_final = wavs[0]

    segment_path = "new_segment.wav"
    torchaudio.save(segment_path, wav_final, sr)

    cumulative_path = "generated_audio.wav"
    if os.path.exists(cumulative_path):
        existing_audio, existing_sr = torchaudio.load(cumulative_path)
        if existing_sr != sr:
            print("Sample rate mismatch detected. Overwriting existing file.")
            combined = wav_final
        else:
            combined = torch.cat([existing_audio, wav_final], dim=1)
    else:
        combined = wav_final

    torchaudio.save(cumulative_path, combined, sr)
    print(f"Segment saved to {segment_path} and cumulative audio updated in {cumulative_path}")

    return segment_path, cumulative_path



def advance_story(choice_index, current_node_id, voice_sample_path, speaking_rate, pitch):
    if choice_index == -1:
        return "Story ended. Here is the full audio of your adventure.", current_node_id, [], "generated_audio.wav"

    current_node = story.get(current_node_id)
    if not current_node:
        return "Error: Current node not found.", current_node_id, [], ""

    options = current_node.get("options", [])

    if choice_index < 0 or choice_index >= len(options):
        return "Invalid choice selected.", current_node_id, options, ""

    next_node_id = options[choice_index]["next"]
    next_node = story.get(next_node_id)
    if not next_node:
        return "End of story reached.", current_node_id, [], "generated_audio.wav"

    next_text = next_node.get("text", "")
    next_emotion = next_node.get("emotion", "neutral")

    segment_audio, cumulative_audio = generate_tts_audio(
        text=next_text,
        voice_sample_path=voice_sample_path,
        emotion=next_emotion,
        speaking_rate=speaking_rate,
        pitch=pitch
    )

    next_options = [opt["choice"] for opt in next_node.get("options", [])]
    return next_text, next_node_id, next_options, segment_audio



def start_story(voice_sample_path, speaking_rate, pitch):
    current_node_id = "start"
    node = story.get(current_node_id)
    text = node.get("text", "")
    emotion = node.get("emotion", "neutral")

    segment_audio, cumulative_audio = generate_tts_audio(
        text=text,
        voice_sample_path=voice_sample_path,
        emotion=emotion,
        speaking_rate=speaking_rate,
        pitch=pitch
    )
    options = [opt["choice"] for opt in node.get("options", [])]
    return text, current_node_id, options, segment_audio


import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## VoxVoyage: Crafting Your Adventures with Every Word")

    with gr.Row():
        voice_sample_input = gr.File(label="Upload Voice Sample (for voice cloning)", file_types=["audio"])
        speaking_rate_slider = gr.Slider(minimum=0.5, maximum=2.0, value=1.0, step=0.1, label="Speaking Rate")
        pitch_slider = gr.Slider(minimum=0.5, maximum=2.0, value=1.0, step=0.1, label="Pitch")

    with gr.Row():
        start_button = gr.Button("Start Story")
        advance_button = gr.Button("Advance Story")
        quit_button = gr.Button("Quit Story")

    story_text = gr.Textbox(label="Story Narrative", interactive=False, lines=4)
    options_radio = gr.Radio(choices=[], label="Choose an Option")
    audio_output = gr.Audio(label="Generated Speech", type="filepath")

    current_node_state = gr.State("start")

    def start_callback(voice_file, speaking_rate, pitch):
        if voice_file is None:
            return "Please upload a voice sample to start the story.", "start", gr.update(choices=[]), ""
        voice_path = voice_file["name"] if isinstance(voice_file, dict) else voice_file
        text, node_id, options, segment_audio = start_story(voice_path, speaking_rate, pitch)
        radio_update = gr.update(choices=options, value=options[0] if options else None)
        return text, node_id, radio_update, segment_audio

    start_button.click(
        start_callback,
        inputs=[voice_sample_input, speaking_rate_slider, pitch_slider],
        outputs=[story_text, current_node_state, options_radio, audio_output]
    )

    def advance_callback(choice, current_node, voice_file, speaking_rate, pitch):
        if voice_file is None:
            return "Please upload a voice sample.", current_node, gr.update(choices=[]), ""
        voice_path = voice_file["name"] if isinstance(voice_file, dict) else voice_file
        try:
            choice_index = int(choice)
        except Exception as e:
            choice_index = 0
        text, new_node, options, segment_audio = advance_story(choice_index, current_node, voice_path, speaking_rate, pitch)
        radio_update = gr.update(choices=options, value=options[0] if options else None)
        return text, new_node, radio_update, segment_audio

    advance_button.click(
        advance_callback,
        inputs=[options_radio, current_node_state, voice_sample_input, speaking_rate_slider, pitch_slider],
        outputs=[story_text, current_node_state, options_radio, audio_output]
    )

    def quit_callback(current_node, voice_file, speaking_rate, pitch):
        if voice_file is None:
            return "Please upload a voice sample.", current_node, gr.update(choices=[]), ""
        voice_path = voice_file["name"] if isinstance(voice_file, dict) else voice_file
        text, new_node, options, audio = advance_story(-1, current_node, voice_path, speaking_rate, pitch)
        radio_update = gr.update(choices=options, value=None)
        return text, new_node, radio_update, audio

    quit_button.click(
        quit_callback,
        inputs=[current_node_state, voice_sample_input, speaking_rate_slider, pitch_slider],
        outputs=[story_text, current_node_state, options_radio, audio_output]
    )


demo.launch()