# Custom Selector for ComfyUI

このカスタムノードは、次のノードを含んでいます。

- Text Selector: 複数行のテキストより、指定された行のみを出力するノード
- Text Map Selector: 複数行のテキスト(Key:Value形式)より、指定されたキーに対応する Value を出力するノード
- Number Generator: 数値を生成するノード(seed のみのノードとなります)
- Number Filter: 入力された数値の範囲を制限するノード
- To Int: 文字列(STRING)を数値(INT)に変換するノード
- To String: 数値(INT)を文字列(STRING)に変換するノード
- Checkpoint Loader Simple From String: Checkpoint Loader Simple とほぼ同じですが、checkpoint を文字列より入力可能としたノード
- LoRA Loader From String: LoRA Loader とほぼ同じですが、 lora_name を文字列より入力可能としたノード

何ができるか？
- Checkpoint, LoRA, 基本的なプロンプトの組み合わせを用意し、どの組み合わせを利用するか簡単に切替、あるいはランダム利用可能となります。

例)
　パターン:A-001: Checkpoint: A, LoRA: A-X を利用する場合、最低限 prompt に、 xyz を指定した方が良い。
　パターン:B-001, 002, 003  : Checkpoint: B には、LoRA: B-X, B-Y, B-Z が利用できる。
　パターン:C-001, 002       : Checkpoint: C には、LoRA: C-X, C-Y が利用でき、最低限 prompt に、abc を指定した方が良い。
 上記なような設定をカスタムノードを組み合わせて設定可能
