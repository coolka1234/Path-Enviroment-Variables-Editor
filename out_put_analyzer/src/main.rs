use std::collections::{HashMap};
use std::env;
use std::error::Error;
use std::fs::File;
use std::io::{self, BufRead, Write};
use serde::{Serialize, Deserialize};
use serde_json;
#[derive(Serialize, Deserialize, Debug)]
struct FileAnalysis {
    file_path: String,
    num_characters: usize,
    most_common_word: Option<String>,
    most_common_char: Option<char>,
    least_common_char: Option<char>,
    num_rows: usize,
    num_words: usize,
}
//cargo run --release C:\Users\krzys\OneDrive\Pulpit\Studia\Semestr4\SkryptoweLab\Lista4\Araujo.txt
fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} <file_path>", args[0]);
        return;
    }
    let file_path = &args[1];
    if let Ok(analysis) = analyze_file(file_path) {
        println!("{:#?}", &analysis);
        if let Err(err) = write_to_json(&analysis, "output.json") {
            eprintln!("Error writing to JSON file: {}", err);
        }
    } else {
        eprintln!("Error analyzing the file.");
    }
}
fn analyze_file(file_path: &str) -> Result<FileAnalysis, Box<dyn Error>> {
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    let mut word_count_map: HashMap<String, usize> = HashMap::new();
    let mut char_count_map: HashMap<char, usize> = HashMap::new();
    let mut total_chars = 0;
    let mut num_rows = 0;
    let mut num_words = 0;

    for line in reader.lines() {
        let line = line?;
        num_rows += 1;
        let words: Vec<&str> = line.split_whitespace().collect();
        num_words += words.len();

        for c in line.chars() {
            if c.is_whitespace() {
                continue;
            }
            *char_count_map.entry(c).or_insert(0) += 1;
            total_chars += 1;
        }

        for word in words {
            *word_count_map.entry(word.to_string()).or_insert(0) += 1;
        }
    }

    let most_common_word = word_count_map
        .iter()
        .max_by_key(|&(_, count)| count)
        .map(|(word, _)| word.to_string());

    let most_common_char = char_count_map
        .iter()
        .max_by_key(|&(_, count)| count)
        .map(|(char, _)| *char);

    let least_common_char = char_count_map
        .iter()
        .min_by_key(|&(_, count)| count)
        .map(|(char, _)| *char);

    let analysis = FileAnalysis {
        file_path: String::from(file_path),
        num_characters: total_chars,
        most_common_word,
        most_common_char,
        least_common_char,
        num_rows,
        num_words,
    };

    Ok(analysis)
}
fn write_to_json(analysis: &FileAnalysis, output_path: &str) -> Result<(), Box<dyn Error>> {
    let json_output = serde_json::to_string_pretty(analysis)?;

    let mut output_file = File::create(output_path)?;
    output_file.write_all(json_output.as_bytes())?;
    println!("Analysis result written to {}", output_path);
    Ok(())
}
